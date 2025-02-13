import { i as Ce, a as J, r as Re, g as je, w as A, b as Se } from "./Index-CT37_FQ1.js";
const P = window.ms_globals.React, be = window.ms_globals.React.forwardRef, ye = window.ms_globals.React.useRef, we = window.ms_globals.React.useState, Ee = window.ms_globals.React.useEffect, j = window.ms_globals.React.useMemo, q = window.ms_globals.ReactDOM.createPortal, ke = window.ms_globals.internalContext.useContextPropsContext, U = window.ms_globals.internalContext.ContextPropsProvider, Oe = window.ms_globals.antd.DatePicker, Q = window.ms_globals.dayjs, Pe = window.ms_globals.createItemsContext.createItemsContext;
var Te = /\s/;
function Fe(e) {
  for (var t = e.length; t-- && Te.test(e.charAt(t)); )
    ;
  return t;
}
var De = /^\s+/;
function Le(e) {
  return e && e.slice(0, Fe(e) + 1).replace(De, "");
}
var Z = NaN, Ne = /^[-+]0x[0-9a-f]+$/i, Ae = /^0b[01]+$/i, We = /^0o[0-7]+$/i, Me = parseInt;
function V(e) {
  if (typeof e == "number")
    return e;
  if (Ce(e))
    return Z;
  if (J(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = J(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Le(e);
  var s = Ae.test(e);
  return s || We.test(e) ? Me(e.slice(2), s ? 2 : 8) : Ne.test(e) ? Z : +e;
}
var H = function() {
  return Re.Date.now();
}, Ue = "Expected a function", Be = Math.max, He = Math.min;
function ze(e, t, s) {
  var i, o, n, r, l, u, x = 0, _ = !1, c = !1, I = !0;
  if (typeof e != "function")
    throw new TypeError(Ue);
  t = V(t) || 0, J(s) && (_ = !!s.leading, c = "maxWait" in s, n = c ? Be(V(s.maxWait) || 0, t) : n, I = "trailing" in s ? !!s.trailing : I);
  function d(p) {
    var E = i, O = o;
    return i = o = void 0, x = p, r = e.apply(O, E), r;
  }
  function b(p) {
    return x = p, l = setTimeout(h, t), _ ? d(p) : r;
  }
  function f(p) {
    var E = p - u, O = p - x, D = t - E;
    return c ? He(D, n - O) : D;
  }
  function m(p) {
    var E = p - u, O = p - x;
    return u === void 0 || E >= t || E < 0 || c && O >= n;
  }
  function h() {
    var p = H();
    if (m(p))
      return y(p);
    l = setTimeout(h, f(p));
  }
  function y(p) {
    return l = void 0, I && i ? d(p) : (i = o = void 0, r);
  }
  function S() {
    l !== void 0 && clearTimeout(l), x = 0, i = u = o = l = void 0;
  }
  function a() {
    return l === void 0 ? r : y(H());
  }
  function k() {
    var p = H(), E = m(p);
    if (i = arguments, o = this, u = p, E) {
      if (l === void 0)
        return b(u);
      if (c)
        return clearTimeout(l), l = setTimeout(h, t), d(u);
    }
    return l === void 0 && (l = setTimeout(h, t)), r;
  }
  return k.cancel = S, k.flush = a, k;
}
var ce = {
  exports: {}
}, B = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ge = P, qe = Symbol.for("react.element"), Je = Symbol.for("react.fragment"), Xe = Object.prototype.hasOwnProperty, Ye = Ge.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ke = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ae(e, t, s) {
  var i, o = {}, n = null, r = null;
  s !== void 0 && (n = "" + s), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Xe.call(t, i) && !Ke.hasOwnProperty(i) && (o[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) o[i] === void 0 && (o[i] = t[i]);
  return {
    $$typeof: qe,
    type: e,
    key: n,
    ref: r,
    props: o,
    _owner: Ye.current
  };
}
B.Fragment = Je;
B.jsx = ae;
B.jsxs = ae;
ce.exports = B;
var v = ce.exports;
const {
  SvelteComponent: Qe,
  assign: $,
  binding_callbacks: ee,
  check_outros: Ze,
  children: ue,
  claim_element: fe,
  claim_space: Ve,
  component_subscribe: te,
  compute_slots: $e,
  create_slot: et,
  detach: F,
  element: de,
  empty: ne,
  exclude_internal_props: re,
  get_all_dirty_from_scope: tt,
  get_slot_changes: nt,
  group_outros: rt,
  init: ot,
  insert_hydration: W,
  safe_not_equal: st,
  set_custom_element_data: me,
  space: it,
  transition_in: M,
  transition_out: X,
  update_slot_base: lt
} = window.__gradio__svelte__internal, {
  beforeUpdate: ct,
  getContext: at,
  onDestroy: ut,
  setContext: ft
} = window.__gradio__svelte__internal;
function oe(e) {
  let t, s;
  const i = (
    /*#slots*/
    e[7].default
  ), o = et(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = de("svelte-slot"), o && o.c(), this.h();
    },
    l(n) {
      t = fe(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ue(t);
      o && o.l(r), r.forEach(F), this.h();
    },
    h() {
      me(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      W(n, t, r), o && o.m(t, null), e[9](t), s = !0;
    },
    p(n, r) {
      o && o.p && (!s || r & /*$$scope*/
      64) && lt(
        o,
        i,
        n,
        /*$$scope*/
        n[6],
        s ? nt(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : tt(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      s || (M(o, n), s = !0);
    },
    o(n) {
      X(o, n), s = !1;
    },
    d(n) {
      n && F(t), o && o.d(n), e[9](null);
    }
  };
}
function dt(e) {
  let t, s, i, o, n = (
    /*$$slots*/
    e[4].default && oe(e)
  );
  return {
    c() {
      t = de("react-portal-target"), s = it(), n && n.c(), i = ne(), this.h();
    },
    l(r) {
      t = fe(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ue(t).forEach(F), s = Ve(r), n && n.l(r), i = ne(), this.h();
    },
    h() {
      me(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      W(r, t, l), e[8](t), W(r, s, l), n && n.m(r, l), W(r, i, l), o = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && M(n, 1)) : (n = oe(r), n.c(), M(n, 1), n.m(i.parentNode, i)) : n && (rt(), X(n, 1, 1, () => {
        n = null;
      }), Ze());
    },
    i(r) {
      o || (M(n), o = !0);
    },
    o(r) {
      X(n), o = !1;
    },
    d(r) {
      r && (F(t), F(s), F(i)), e[8](null), n && n.d(r);
    }
  };
}
function se(e) {
  const {
    svelteInit: t,
    ...s
  } = e;
  return s;
}
function mt(e, t, s) {
  let i, o, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = $e(n);
  let {
    svelteInit: u
  } = t;
  const x = A(se(t)), _ = A();
  te(e, _, (a) => s(0, i = a));
  const c = A();
  te(e, c, (a) => s(1, o = a));
  const I = [], d = at("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: f,
    subSlotIndex: m
  } = je() || {}, h = u({
    parent: d,
    props: x,
    target: _,
    slot: c,
    slotKey: b,
    slotIndex: f,
    subSlotIndex: m,
    onDestroy(a) {
      I.push(a);
    }
  });
  ft("$$ms-gr-react-wrapper", h), ct(() => {
    x.set(se(t));
  }), ut(() => {
    I.forEach((a) => a());
  });
  function y(a) {
    ee[a ? "unshift" : "push"](() => {
      i = a, _.set(i);
    });
  }
  function S(a) {
    ee[a ? "unshift" : "push"](() => {
      o = a, c.set(o);
    });
  }
  return e.$$set = (a) => {
    s(17, t = $($({}, t), re(a))), "svelteInit" in a && s(5, u = a.svelteInit), "$$scope" in a && s(6, r = a.$$scope);
  }, t = re(t), [i, o, _, c, l, u, r, n, y, S];
}
class pt extends Qe {
  constructor(t) {
    super(), ot(this, t, mt, dt, st, {
      svelteInit: 5
    });
  }
}
const ie = window.ms_globals.rerender, z = window.ms_globals.tree;
function _t(e, t = {}) {
  function s(i) {
    const o = A(), n = new pt({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
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
          return u.nodes = [...u.nodes, l], ie({
            createPortal: q,
            node: z
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((x) => x.svelteInstance !== o), ie({
              createPortal: q,
              node: z
            });
          }), l;
        },
        ...i.props
      }
    });
    return o.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(s);
    });
  });
}
const ht = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function xt(e) {
  return e ? Object.keys(e).reduce((t, s) => {
    const i = e[s];
    return t[s] = gt(s, i), t;
  }, {}) : {};
}
function gt(e, t) {
  return typeof t == "number" && !ht.includes(e) ? t + "px" : t;
}
function Y(e) {
  const t = [], s = e.cloneNode(!1);
  if (e._reactElement) {
    const o = P.Children.toArray(e._reactElement.props.children).map((n) => {
      if (P.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = Y(n.props.el);
        return P.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...P.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return o.originalChildren = e._reactElement.props.children, t.push(q(P.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: o
    }), s)), {
      clonedElement: s,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((o) => {
    e.getEventListeners(o).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      s.addEventListener(l, r, u);
    });
  });
  const i = Array.from(e.childNodes);
  for (let o = 0; o < i.length; o++) {
    const n = i[o];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = Y(n);
      t.push(...l), s.appendChild(r);
    } else n.nodeType === 3 && s.appendChild(n.cloneNode());
  }
  return {
    clonedElement: s,
    portals: t
  };
}
function vt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const w = be(({
  slot: e,
  clone: t,
  className: s,
  style: i,
  observeAttributes: o
}, n) => {
  const r = ye(), [l, u] = we([]), {
    forceClone: x
  } = ke(), _ = x ? !0 : t;
  return Ee(() => {
    var b;
    if (!r.current || !e)
      return;
    let c = e;
    function I() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), vt(n, f), s && f.classList.add(...s.split(" ")), i) {
        const m = xt(i);
        Object.keys(m).forEach((h) => {
          f.style[h] = m[h];
        });
      }
    }
    let d = null;
    if (_ && window.MutationObserver) {
      let f = function() {
        var S, a, k;
        (S = r.current) != null && S.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: h,
          clonedElement: y
        } = Y(e);
        c = y, u(h), c.style.display = "contents", I(), (k = r.current) == null || k.appendChild(c);
      };
      f();
      const m = ze(() => {
        f(), d == null || d.disconnect(), d == null || d.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      d = new window.MutationObserver(m), d.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", I(), (b = r.current) == null || b.appendChild(c);
    return () => {
      var f, m;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((m = r.current) == null || m.removeChild(c)), d == null || d.disconnect();
    };
  }, [e, _, s, i, n, o]), P.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function It(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function bt(e, t = !1) {
  try {
    if (Se(e))
      return e;
    if (t && !It(e))
      return;
    if (typeof e == "string") {
      let s = e.trim();
      return s.startsWith(";") && (s = s.slice(1)), s.endsWith(";") && (s = s.slice(0, -1)), new Function(`return (...args) => (${s})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function L(e, t) {
  return j(() => bt(e, t), [e, t]);
}
function pe(e, t, s) {
  const i = e.filter(Boolean);
  if (i.length !== 0)
    return i.map((o, n) => {
      var x;
      if (typeof o != "object")
        return o;
      const r = {
        ...o.props,
        key: ((x = o.props) == null ? void 0 : x.key) ?? (s ? `${s}-${n}` : `${n}`)
      };
      let l = r;
      Object.keys(o.slots).forEach((_) => {
        if (!o.slots[_] || !(o.slots[_] instanceof Element) && !o.slots[_].el)
          return;
        const c = _.split(".");
        c.forEach((h, y) => {
          l[h] || (l[h] = {}), y !== c.length - 1 && (l = r[h]);
        });
        const I = o.slots[_];
        let d, b, f = !1, m = t == null ? void 0 : t.forceClone;
        I instanceof Element ? d = I : (d = I.el, b = I.callback, f = I.clone ?? f, m = I.forceClone ?? m), m = m ?? !!b, l[c[c.length - 1]] = d ? b ? (...h) => (b(c[c.length - 1], h), /* @__PURE__ */ v.jsx(U, {
          params: h,
          forceClone: m,
          children: /* @__PURE__ */ v.jsx(w, {
            slot: d,
            clone: f
          })
        })) : /* @__PURE__ */ v.jsx(U, {
          forceClone: m,
          children: /* @__PURE__ */ v.jsx(w, {
            slot: d,
            clone: f
          })
        }) : l[c[c.length - 1]], l = r;
      });
      const u = "children";
      return o[u] && (r[u] = pe(o[u], t, `${n}`)), r;
    });
}
function le(e, t) {
  return e ? /* @__PURE__ */ v.jsx(w, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function G({
  key: e,
  slots: t,
  targets: s
}, i) {
  return t[e] ? (...o) => s ? s.map((n, r) => /* @__PURE__ */ v.jsx(U, {
    params: o,
    forceClone: !0,
    children: le(n, {
      clone: !0,
      ...i
    })
  }, r)) : /* @__PURE__ */ v.jsx(U, {
    params: o,
    forceClone: !0,
    children: le(t[e], {
      clone: !0,
      ...i
    })
  }) : void 0;
}
const {
  withItemsContextProvider: yt,
  useItems: wt,
  ItemHandler: Ct
} = Pe("antd-date-picker-presets");
function R(e) {
  return Q(typeof e == "number" ? e * 1e3 : e);
}
function N(e) {
  return (e == null ? void 0 : e.map((t) => t ? t.valueOf() / 1e3 : null)) || [null, null];
}
const Rt = _t(yt(["presets"], ({
  slots: e,
  disabledDate: t,
  value: s,
  defaultValue: i,
  defaultPickerValue: o,
  pickerValue: n,
  presets: r,
  showTime: l,
  onChange: u,
  minDate: x,
  maxDate: _,
  cellRender: c,
  panelRender: I,
  getPopupContainer: d,
  onValueChange: b,
  onPanelChange: f,
  onCalendarChange: m,
  children: h,
  setSlotParams: y,
  elRef: S,
  ...a
}) => {
  const k = L(t), p = L(d), E = L(c), O = L(I), D = j(() => {
    var g;
    return typeof l == "object" ? {
      ...l,
      defaultValue: (g = l.defaultValue) == null ? void 0 : g.map((C) => R(C))
    } : l;
  }, [l]), _e = j(() => s == null ? void 0 : s.map((g) => R(g)), [s]), he = j(() => i == null ? void 0 : i.map((g) => R(g)), [i]), xe = j(() => Array.isArray(o) ? o.map((g) => R(g)) : o ? R(o) : void 0, [o]), ge = j(() => Array.isArray(n) ? n.map((g) => R(g)) : n ? R(n) : void 0, [n]), ve = j(() => x ? R(x) : void 0, [x]), Ie = j(() => _ ? R(_) : void 0, [_]), {
    items: {
      presets: K
    }
  } = wt();
  return /* @__PURE__ */ v.jsxs(v.Fragment, {
    children: [/* @__PURE__ */ v.jsx("div", {
      style: {
        display: "none"
      },
      children: h
    }), /* @__PURE__ */ v.jsx(Oe.RangePicker, {
      ...a,
      ref: S,
      value: _e,
      defaultValue: he,
      defaultPickerValue: xe,
      pickerValue: ge,
      minDate: ve,
      maxDate: Ie,
      showTime: D,
      disabledDate: k,
      getPopupContainer: p,
      cellRender: e.cellRender ? G({
        slots: e,
        setSlotParams: y,
        key: "cellRender"
      }) : E,
      panelRender: e.panelRender ? G({
        slots: e,
        setSlotParams: y,
        key: "panelRender"
      }) : O,
      presets: j(() => {
        var g;
        return (g = r || pe(K)) == null ? void 0 : g.map((C) => ({
          ...C,
          value: N(C.value)
        }));
      }, [r, K]),
      onPanelChange: (g, ...C) => {
        const T = N(g);
        f == null || f(T, ...C);
      },
      onChange: (g, ...C) => {
        const T = N(g);
        u == null || u(T, ...C), b(T);
      },
      onCalendarChange: (g, ...C) => {
        const T = N(g);
        m == null || m(T, ...C);
      },
      renderExtraFooter: e.renderExtraFooter ? G({
        slots: e,
        setSlotParams: y,
        key: "renderExtraFooter"
      }) : a.renderExtraFooter,
      prefix: e.prefix ? /* @__PURE__ */ v.jsx(w, {
        slot: e.prefix
      }) : a.prefix,
      prevIcon: e.prevIcon ? /* @__PURE__ */ v.jsx(w, {
        slot: e.prevIcon
      }) : a.prevIcon,
      nextIcon: e.nextIcon ? /* @__PURE__ */ v.jsx(w, {
        slot: e.nextIcon
      }) : a.nextIcon,
      suffixIcon: e.suffixIcon ? /* @__PURE__ */ v.jsx(w, {
        slot: e.suffixIcon
      }) : a.suffixIcon,
      superNextIcon: e.superNextIcon ? /* @__PURE__ */ v.jsx(w, {
        slot: e.superNextIcon
      }) : a.superNextIcon,
      superPrevIcon: e.superPrevIcon ? /* @__PURE__ */ v.jsx(w, {
        slot: e.superPrevIcon
      }) : a.superPrevIcon,
      allowClear: e["allowClear.clearIcon"] ? {
        clearIcon: /* @__PURE__ */ v.jsx(w, {
          slot: e["allowClear.clearIcon"]
        })
      } : a.allowClear,
      separator: e.separator ? /* @__PURE__ */ v.jsx(w, {
        slot: e.separator,
        clone: !0
      }) : a.separator
    })]
  });
}));
export {
  Rt as DateRangePicker,
  Rt as default
};
