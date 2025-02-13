import { i as be, a as H, r as Ie, g as Ee, w as A, b as Re } from "./Index-rJS4Y3ti.js";
const O = window.ms_globals.React, ge = window.ms_globals.React.forwardRef, ve = window.ms_globals.React.useRef, we = window.ms_globals.React.useState, ye = window.ms_globals.React.useEffect, P = window.ms_globals.React.useMemo, G = window.ms_globals.ReactDOM.createPortal, Ce = window.ms_globals.internalContext.useContextPropsContext, J = window.ms_globals.internalContext.ContextPropsProvider, Se = window.ms_globals.antd.TimePicker, X = window.ms_globals.dayjs;
var Te = /\s/;
function Pe(e) {
  for (var t = e.length; t-- && Te.test(e.charAt(t)); )
    ;
  return t;
}
var Oe = /^\s+/;
function je(e) {
  return e && e.slice(0, Pe(e) + 1).replace(Oe, "");
}
var Y = NaN, ke = /^[-+]0x[0-9a-f]+$/i, Fe = /^0b[01]+$/i, Le = /^0o[0-7]+$/i, Ne = parseInt;
function Q(e) {
  if (typeof e == "number")
    return e;
  if (be(e))
    return Y;
  if (H(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = H(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = je(e);
  var o = Fe.test(e);
  return o || Le.test(e) ? Ne(e.slice(2), o ? 2 : 8) : ke.test(e) ? Y : +e;
}
var U = function() {
  return Ie.Date.now();
}, Ae = "Expected a function", De = Math.max, We = Math.min;
function Me(e, t, o) {
  var s, i, n, r, l, u, p = 0, w = !1, c = !1, y = !0;
  if (typeof e != "function")
    throw new TypeError(Ae);
  t = Q(t) || 0, H(o) && (w = !!o.leading, c = "maxWait" in o, n = c ? De(Q(o.maxWait) || 0, t) : n, y = "trailing" in o ? !!o.trailing : y);
  function m(f) {
    var I = s, T = i;
    return s = i = void 0, p = f, r = e.apply(T, I), r;
  }
  function b(f) {
    return p = f, l = setTimeout(g, t), w ? m(f) : r;
  }
  function d(f) {
    var I = f - u, T = f - p, N = t - I;
    return c ? We(N, n - T) : N;
  }
  function x(f) {
    var I = f - u, T = f - p;
    return u === void 0 || I >= t || I < 0 || c && T >= n;
  }
  function g() {
    var f = U();
    if (x(f))
      return R(f);
    l = setTimeout(g, d(f));
  }
  function R(f) {
    return l = void 0, y && s ? m(f) : (s = i = void 0, r);
  }
  function _() {
    l !== void 0 && clearTimeout(l), p = 0, s = u = i = l = void 0;
  }
  function a() {
    return l === void 0 ? r : R(U());
  }
  function C() {
    var f = U(), I = x(f);
    if (s = arguments, i = this, u = f, I) {
      if (l === void 0)
        return b(u);
      if (c)
        return clearTimeout(l), l = setTimeout(g, t), m(u);
    }
    return l === void 0 && (l = setTimeout(g, t)), r;
  }
  return C.cancel = _, C.flush = a, C;
}
var le = {
  exports: {}
}, M = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ue = O, ze = Symbol.for("react.element"), Be = Symbol.for("react.fragment"), Ge = Object.prototype.hasOwnProperty, He = Ue.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ke = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ce(e, t, o) {
  var s, i = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (s in t) Ge.call(t, s) && !Ke.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: ze,
    type: e,
    key: n,
    ref: r,
    props: i,
    _owner: He.current
  };
}
M.Fragment = Be;
M.jsx = ce;
M.jsxs = ce;
le.exports = M;
var h = le.exports;
const {
  SvelteComponent: qe,
  assign: Z,
  binding_callbacks: V,
  check_outros: Je,
  children: ae,
  claim_element: ue,
  claim_space: Xe,
  component_subscribe: $,
  compute_slots: Ye,
  create_slot: Qe,
  detach: k,
  element: de,
  empty: ee,
  exclude_internal_props: te,
  get_all_dirty_from_scope: Ze,
  get_slot_changes: Ve,
  group_outros: $e,
  init: et,
  insert_hydration: D,
  safe_not_equal: tt,
  set_custom_element_data: fe,
  space: nt,
  transition_in: W,
  transition_out: K,
  update_slot_base: rt
} = window.__gradio__svelte__internal, {
  beforeUpdate: ot,
  getContext: it,
  onDestroy: st,
  setContext: lt
} = window.__gradio__svelte__internal;
function ne(e) {
  let t, o;
  const s = (
    /*#slots*/
    e[7].default
  ), i = Qe(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = de("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = ue(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ae(t);
      i && i.l(r), r.forEach(k), this.h();
    },
    h() {
      fe(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      D(n, t, r), i && i.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      i && i.p && (!o || r & /*$$scope*/
      64) && rt(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        o ? Ve(
          s,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Ze(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (W(i, n), o = !0);
    },
    o(n) {
      K(i, n), o = !1;
    },
    d(n) {
      n && k(t), i && i.d(n), e[9](null);
    }
  };
}
function ct(e) {
  let t, o, s, i, n = (
    /*$$slots*/
    e[4].default && ne(e)
  );
  return {
    c() {
      t = de("react-portal-target"), o = nt(), n && n.c(), s = ee(), this.h();
    },
    l(r) {
      t = ue(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ae(t).forEach(k), o = Xe(r), n && n.l(r), s = ee(), this.h();
    },
    h() {
      fe(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      D(r, t, l), e[8](t), D(r, o, l), n && n.m(r, l), D(r, s, l), i = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && W(n, 1)) : (n = ne(r), n.c(), W(n, 1), n.m(s.parentNode, s)) : n && ($e(), K(n, 1, 1, () => {
        n = null;
      }), Je());
    },
    i(r) {
      i || (W(n), i = !0);
    },
    o(r) {
      K(n), i = !1;
    },
    d(r) {
      r && (k(t), k(o), k(s)), e[8](null), n && n.d(r);
    }
  };
}
function re(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function at(e, t, o) {
  let s, i, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Ye(n);
  let {
    svelteInit: u
  } = t;
  const p = A(re(t)), w = A();
  $(e, w, (a) => o(0, s = a));
  const c = A();
  $(e, c, (a) => o(1, i = a));
  const y = [], m = it("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: d,
    subSlotIndex: x
  } = Ee() || {}, g = u({
    parent: m,
    props: p,
    target: w,
    slot: c,
    slotKey: b,
    slotIndex: d,
    subSlotIndex: x,
    onDestroy(a) {
      y.push(a);
    }
  });
  lt("$$ms-gr-react-wrapper", g), ot(() => {
    p.set(re(t));
  }), st(() => {
    y.forEach((a) => a());
  });
  function R(a) {
    V[a ? "unshift" : "push"](() => {
      s = a, w.set(s);
    });
  }
  function _(a) {
    V[a ? "unshift" : "push"](() => {
      i = a, c.set(i);
    });
  }
  return e.$$set = (a) => {
    o(17, t = Z(Z({}, t), te(a))), "svelteInit" in a && o(5, u = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = te(t), [s, i, w, c, l, u, r, n, R, _];
}
class ut extends qe {
  constructor(t) {
    super(), et(this, t, at, ct, tt, {
      svelteInit: 5
    });
  }
}
const oe = window.ms_globals.rerender, z = window.ms_globals.tree;
function dt(e, t = {}) {
  function o(s) {
    const i = A(), n = new ut({
      ...s,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? z;
          return u.nodes = [...u.nodes, l], oe({
            createPortal: G,
            node: z
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((p) => p.svelteInstance !== i), oe({
              createPortal: G,
              node: z
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(o);
    });
  });
}
const ft = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function mt(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const s = e[o];
    return t[o] = pt(o, s), t;
  }, {}) : {};
}
function pt(e, t) {
  return typeof t == "number" && !ft.includes(e) ? t + "px" : t;
}
function q(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const i = O.Children.toArray(e._reactElement.props.children).map((n) => {
      if (O.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = q(n.props.el);
        return O.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...O.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(G(O.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = q(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function _t(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const E = ge(({
  slot: e,
  clone: t,
  className: o,
  style: s,
  observeAttributes: i
}, n) => {
  const r = ve(), [l, u] = we([]), {
    forceClone: p
  } = Ce(), w = p ? !0 : t;
  return ye(() => {
    var b;
    if (!r.current || !e)
      return;
    let c = e;
    function y() {
      let d = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (d = c.children[0], d.tagName.toLowerCase() === "react-portal-target" && d.children[0] && (d = d.children[0])), _t(n, d), o && d.classList.add(...o.split(" ")), s) {
        const x = mt(s);
        Object.keys(x).forEach((g) => {
          d.style[g] = x[g];
        });
      }
    }
    let m = null;
    if (w && window.MutationObserver) {
      let d = function() {
        var _, a, C;
        (_ = r.current) != null && _.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: g,
          clonedElement: R
        } = q(e);
        c = R, u(g), c.style.display = "contents", y(), (C = r.current) == null || C.appendChild(c);
      };
      d();
      const x = Me(() => {
        d(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      m = new window.MutationObserver(x), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", y(), (b = r.current) == null || b.appendChild(c);
    return () => {
      var d, x;
      c.style.display = "", (d = r.current) != null && d.contains(c) && ((x = r.current) == null || x.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, w, o, s, n, i]), O.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function ht(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function xt(e, t = !1) {
  try {
    if (Re(e))
      return e;
    if (t && !ht(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function L(e, t) {
  return P(() => xt(e, t), [e, t]);
}
function ie(e, t) {
  return e ? /* @__PURE__ */ h.jsx(E, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function se({
  key: e,
  slots: t,
  targets: o
}, s) {
  return t[e] ? (...i) => o ? o.map((n, r) => /* @__PURE__ */ h.jsx(J, {
    params: i,
    forceClone: !0,
    children: ie(n, {
      clone: !0,
      ...s
    })
  }, r)) : /* @__PURE__ */ h.jsx(J, {
    params: i,
    forceClone: !0,
    children: ie(t[e], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
function S(e) {
  return X(typeof e == "number" ? e * 1e3 : e);
}
function B(e) {
  return (e == null ? void 0 : e.map((t) => t ? t.valueOf() / 1e3 : null)) || [null, null];
}
const vt = dt(({
  slots: e,
  disabledDate: t,
  disabledTime: o,
  value: s,
  defaultValue: i,
  defaultPickerValue: n,
  pickerValue: r,
  onChange: l,
  minDate: u,
  maxDate: p,
  cellRender: w,
  panelRender: c,
  getPopupContainer: y,
  onValueChange: m,
  onPanelChange: b,
  onCalendarChange: d,
  children: x,
  setSlotParams: g,
  elRef: R,
  ..._
}) => {
  const a = L(t), C = L(y), f = L(w), I = L(c), T = L(o), N = P(() => s == null ? void 0 : s.map((v) => S(v)), [s]), me = P(() => i == null ? void 0 : i.map((v) => S(v)), [i]), pe = P(() => Array.isArray(n) ? n.map((v) => S(v)) : n ? S(n) : void 0, [n]), _e = P(() => Array.isArray(r) ? r.map((v) => S(v)) : r ? S(r) : void 0, [r]), he = P(() => u ? S(u) : void 0, [u]), xe = P(() => p ? S(p) : void 0, [p]);
  return /* @__PURE__ */ h.jsxs(h.Fragment, {
    children: [/* @__PURE__ */ h.jsx("div", {
      style: {
        display: "none"
      },
      children: x
    }), /* @__PURE__ */ h.jsx(Se.RangePicker, {
      ..._,
      ref: R,
      value: N,
      disabledTime: T,
      defaultValue: me,
      defaultPickerValue: pe,
      pickerValue: _e,
      minDate: he,
      maxDate: xe,
      disabledDate: a,
      getPopupContainer: C,
      cellRender: e.cellRender ? se({
        slots: e,
        setSlotParams: g,
        key: "cellRender"
      }) : f,
      panelRender: e.panelRender ? se({
        slots: e,
        setSlotParams: g,
        key: "panelRender"
      }) : I,
      onPanelChange: (v, ...F) => {
        const j = B(v);
        b == null || b(j, ...F);
      },
      onChange: (v, ...F) => {
        const j = B(v);
        l == null || l(j, ...F), m(j);
      },
      onCalendarChange: (v, ...F) => {
        const j = B(v);
        d == null || d(j, ...F);
      },
      renderExtraFooter: e.renderExtraFooter ? () => e.renderExtraFooter ? /* @__PURE__ */ h.jsx(E, {
        slot: e.renderExtraFooter
      }) : null : _.renderExtraFooter,
      prevIcon: e.prevIcon ? /* @__PURE__ */ h.jsx(E, {
        slot: e.prevIcon
      }) : _.prevIcon,
      nextIcon: e.nextIcon ? /* @__PURE__ */ h.jsx(E, {
        slot: e.nextIcon
      }) : _.nextIcon,
      suffixIcon: e.suffixIcon ? /* @__PURE__ */ h.jsx(E, {
        slot: e.suffixIcon
      }) : _.suffixIcon,
      superNextIcon: e.superNextIcon ? /* @__PURE__ */ h.jsx(E, {
        slot: e.superNextIcon
      }) : _.superNextIcon,
      superPrevIcon: e.superPrevIcon ? /* @__PURE__ */ h.jsx(E, {
        slot: e.superPrevIcon
      }) : _.superPrevIcon,
      allowClear: e["allowClear.clearIcon"] ? {
        clearIcon: /* @__PURE__ */ h.jsx(E, {
          slot: e["allowClear.clearIcon"]
        })
      } : _.allowClear,
      separator: e.separator ? /* @__PURE__ */ h.jsx(E, {
        slot: e.separator
      }) : _.separator
    })]
  });
});
export {
  vt as TimeRangePicker,
  vt as default
};
