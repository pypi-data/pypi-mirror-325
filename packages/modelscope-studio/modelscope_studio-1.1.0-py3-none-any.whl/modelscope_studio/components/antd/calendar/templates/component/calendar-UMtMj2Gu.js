import { i as fe, a as M, r as me, g as pe, w as T, b as _e } from "./Index-DvumFurr.js";
const C = window.ms_globals.React, k = window.ms_globals.React.useMemo, ce = window.ms_globals.React.forwardRef, ae = window.ms_globals.React.useRef, ue = window.ms_globals.React.useState, de = window.ms_globals.React.useEffect, D = window.ms_globals.ReactDOM.createPortal, he = window.ms_globals.internalContext.useContextPropsContext, G = window.ms_globals.internalContext.ContextPropsProvider, ge = window.ms_globals.antd.Calendar, H = window.ms_globals.dayjs;
var ye = /\s/;
function we(e) {
  for (var t = e.length; t-- && ye.test(e.charAt(t)); )
    ;
  return t;
}
var be = /^\s+/;
function ve(e) {
  return e && e.slice(0, we(e) + 1).replace(be, "");
}
var V = NaN, Ee = /^[-+]0x[0-9a-f]+$/i, xe = /^0b[01]+$/i, Ce = /^0o[0-7]+$/i, Re = parseInt;
function K(e) {
  if (typeof e == "number")
    return e;
  if (fe(e))
    return V;
  if (M(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = M(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = ve(e);
  var o = xe.test(e);
  return o || Ce.test(e) ? Re(e.slice(2), o ? 2 : 8) : Ee.test(e) ? V : +e;
}
var F = function() {
  return me.Date.now();
}, Ie = "Expected a function", Oe = Math.max, Se = Math.min;
function ke(e, t, o) {
  var i, s, n, r, l, d, p = 0, y = !1, c = !1, w = !0;
  if (typeof e != "function")
    throw new TypeError(Ie);
  t = K(t) || 0, M(o) && (y = !!o.leading, c = "maxWait" in o, n = c ? Oe(K(o.maxWait) || 0, t) : n, w = "trailing" in o ? !!o.trailing : w);
  function f(a) {
    var h = i, O = s;
    return i = s = void 0, p = a, r = e.apply(O, h), r;
  }
  function b(a) {
    return p = a, l = setTimeout(g, t), y ? f(a) : r;
  }
  function m(a) {
    var h = a - d, O = a - p, B = t - h;
    return c ? Se(B, n - O) : B;
  }
  function _(a) {
    var h = a - d, O = a - p;
    return d === void 0 || h >= t || h < 0 || c && O >= n;
  }
  function g() {
    var a = F();
    if (_(a))
      return v(a);
    l = setTimeout(g, m(a));
  }
  function v(a) {
    return l = void 0, w && i ? f(a) : (i = s = void 0, r);
  }
  function E() {
    l !== void 0 && clearTimeout(l), p = 0, i = d = s = l = void 0;
  }
  function u() {
    return l === void 0 ? r : v(F());
  }
  function x() {
    var a = F(), h = _(a);
    if (i = arguments, s = this, d = a, h) {
      if (l === void 0)
        return b(d);
      if (c)
        return clearTimeout(l), l = setTimeout(g, t), f(d);
    }
    return l === void 0 && (l = setTimeout(g, t)), r;
  }
  return x.cancel = E, x.flush = u, x;
}
var ne = {
  exports: {}
}, j = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Te = C, Le = Symbol.for("react.element"), Pe = Symbol.for("react.fragment"), je = Object.prototype.hasOwnProperty, Fe = Te.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ae = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function re(e, t, o) {
  var i, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) je.call(t, i) && !Ae.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: Le,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: Fe.current
  };
}
j.Fragment = Pe;
j.jsx = re;
j.jsxs = re;
ne.exports = j;
var R = ne.exports;
const {
  SvelteComponent: Ne,
  assign: q,
  binding_callbacks: J,
  check_outros: We,
  children: oe,
  claim_element: se,
  claim_space: De,
  component_subscribe: X,
  compute_slots: Me,
  create_slot: Ue,
  detach: I,
  element: ie,
  empty: Y,
  exclude_internal_props: Q,
  get_all_dirty_from_scope: ze,
  get_slot_changes: Be,
  group_outros: Ge,
  init: He,
  insert_hydration: L,
  safe_not_equal: Ve,
  set_custom_element_data: le,
  space: Ke,
  transition_in: P,
  transition_out: U,
  update_slot_base: qe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Je,
  getContext: Xe,
  onDestroy: Ye,
  setContext: Qe
} = window.__gradio__svelte__internal;
function Z(e) {
  let t, o;
  const i = (
    /*#slots*/
    e[7].default
  ), s = Ue(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ie("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = se(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = oe(t);
      s && s.l(r), r.forEach(I), this.h();
    },
    h() {
      le(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      L(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && qe(
        s,
        i,
        n,
        /*$$scope*/
        n[6],
        o ? Be(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : ze(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (P(s, n), o = !0);
    },
    o(n) {
      U(s, n), o = !1;
    },
    d(n) {
      n && I(t), s && s.d(n), e[9](null);
    }
  };
}
function Ze(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && Z(e)
  );
  return {
    c() {
      t = ie("react-portal-target"), o = Ke(), n && n.c(), i = Y(), this.h();
    },
    l(r) {
      t = se(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), oe(t).forEach(I), o = De(r), n && n.l(r), i = Y(), this.h();
    },
    h() {
      le(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      L(r, t, l), e[8](t), L(r, o, l), n && n.m(r, l), L(r, i, l), s = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && P(n, 1)) : (n = Z(r), n.c(), P(n, 1), n.m(i.parentNode, i)) : n && (Ge(), U(n, 1, 1, () => {
        n = null;
      }), We());
    },
    i(r) {
      s || (P(n), s = !0);
    },
    o(r) {
      U(n), s = !1;
    },
    d(r) {
      r && (I(t), I(o), I(i)), e[8](null), n && n.d(r);
    }
  };
}
function $(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function $e(e, t, o) {
  let i, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Me(n);
  let {
    svelteInit: d
  } = t;
  const p = T($(t)), y = T();
  X(e, y, (u) => o(0, i = u));
  const c = T();
  X(e, c, (u) => o(1, s = u));
  const w = [], f = Xe("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: m,
    subSlotIndex: _
  } = pe() || {}, g = d({
    parent: f,
    props: p,
    target: y,
    slot: c,
    slotKey: b,
    slotIndex: m,
    subSlotIndex: _,
    onDestroy(u) {
      w.push(u);
    }
  });
  Qe("$$ms-gr-react-wrapper", g), Je(() => {
    p.set($(t));
  }), Ye(() => {
    w.forEach((u) => u());
  });
  function v(u) {
    J[u ? "unshift" : "push"](() => {
      i = u, y.set(i);
    });
  }
  function E(u) {
    J[u ? "unshift" : "push"](() => {
      s = u, c.set(s);
    });
  }
  return e.$$set = (u) => {
    o(17, t = q(q({}, t), Q(u))), "svelteInit" in u && o(5, d = u.svelteInit), "$$scope" in u && o(6, r = u.$$scope);
  }, t = Q(t), [i, s, y, c, l, d, r, n, v, E];
}
class et extends Ne {
  constructor(t) {
    super(), He(this, t, $e, Ze, Ve, {
      svelteInit: 5
    });
  }
}
const ee = window.ms_globals.rerender, A = window.ms_globals.tree;
function tt(e, t = {}) {
  function o(i) {
    const s = T(), n = new et({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, d = r.parent ?? A;
          return d.nodes = [...d.nodes, l], ee({
            createPortal: D,
            node: A
          }), r.onDestroy(() => {
            d.nodes = d.nodes.filter((p) => p.svelteInstance !== s), ee({
              createPortal: D,
              node: A
            });
          }), l;
        },
        ...i.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(o);
    });
  });
}
function nt(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function rt(e, t = !1) {
  try {
    if (_e(e))
      return e;
    if (t && !nt(e))
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
function S(e, t) {
  return k(() => rt(e, t), [e, t]);
}
const ot = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function st(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const i = e[o];
    return t[o] = it(o, i), t;
  }, {}) : {};
}
function it(e, t) {
  return typeof t == "number" && !ot.includes(e) ? t + "px" : t;
}
function z(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = C.Children.toArray(e._reactElement.props.children).map((n) => {
      if (C.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = z(n.props.el);
        return C.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...C.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(D(C.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: l,
      useCapture: d
    }) => {
      o.addEventListener(l, r, d);
    });
  });
  const i = Array.from(e.childNodes);
  for (let s = 0; s < i.length; s++) {
    const n = i[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = z(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function lt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const ct = ce(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = ae(), [l, d] = ue([]), {
    forceClone: p
  } = he(), y = p ? !0 : t;
  return de(() => {
    var b;
    if (!r.current || !e)
      return;
    let c = e;
    function w() {
      let m = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (m = c.children[0], m.tagName.toLowerCase() === "react-portal-target" && m.children[0] && (m = m.children[0])), lt(n, m), o && m.classList.add(...o.split(" ")), i) {
        const _ = st(i);
        Object.keys(_).forEach((g) => {
          m.style[g] = _[g];
        });
      }
    }
    let f = null;
    if (y && window.MutationObserver) {
      let m = function() {
        var E, u, x;
        (E = r.current) != null && E.contains(c) && ((u = r.current) == null || u.removeChild(c));
        const {
          portals: g,
          clonedElement: v
        } = z(e);
        c = v, d(g), c.style.display = "contents", w(), (x = r.current) == null || x.appendChild(c);
      };
      m();
      const _ = ke(() => {
        m(), f == null || f.disconnect(), f == null || f.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      f = new window.MutationObserver(_), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", w(), (b = r.current) == null || b.appendChild(c);
    return () => {
      var m, _;
      c.style.display = "", (m = r.current) != null && m.contains(c) && ((_ = r.current) == null || _.removeChild(c)), f == null || f.disconnect();
    };
  }, [e, y, o, i, n, s]), C.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function te(e, t) {
  return e ? /* @__PURE__ */ R.jsx(ct, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function N({
  key: e,
  slots: t,
  targets: o
}, i) {
  return t[e] ? (...s) => o ? o.map((n, r) => /* @__PURE__ */ R.jsx(G, {
    params: s,
    forceClone: !0,
    children: te(n, {
      clone: !0,
      ...i
    })
  }, r)) : /* @__PURE__ */ R.jsx(G, {
    params: s,
    forceClone: !0,
    children: te(t[e], {
      clone: !0,
      ...i
    })
  }) : void 0;
}
function W(e) {
  return H(typeof e == "number" ? e * 1e3 : e);
}
const ut = tt(({
  disabledDate: e,
  value: t,
  defaultValue: o,
  validRange: i,
  onChange: s,
  onPanelChange: n,
  onSelect: r,
  onValueChange: l,
  setSlotParams: d,
  cellRender: p,
  fullCellRender: y,
  headerRender: c,
  children: w,
  slots: f,
  ...b
}) => {
  const m = S(e), _ = S(p), g = S(y), v = S(c), E = k(() => t ? W(t) : void 0, [t]), u = k(() => o ? W(o) : void 0, [o]), x = k(() => Array.isArray(i) ? i.map((a) => W(a)) : void 0, [i]);
  return /* @__PURE__ */ R.jsxs(R.Fragment, {
    children: [/* @__PURE__ */ R.jsx("div", {
      style: {
        display: "none"
      },
      children: w
    }), /* @__PURE__ */ R.jsx(ge, {
      ...b,
      value: E,
      defaultValue: u,
      validRange: x,
      disabledDate: m,
      cellRender: f.cellRender ? N({
        slots: f,
        setSlotParams: d,
        key: "cellRender"
      }) : _,
      fullCellRender: f.fullCellRender ? N({
        slots: f,
        setSlotParams: d,
        key: "fullCellRender"
      }) : g,
      headerRender: f.headerRender ? N({
        slots: f,
        setSlotParams: d,
        key: "headerRender"
      }) : v,
      onChange: (a, ...h) => {
        l(a.valueOf() / 1e3), s == null || s(a.valueOf() / 1e3, ...h);
      },
      onPanelChange: (a, ...h) => {
        n == null || n(a.valueOf() / 1e3, ...h);
      },
      onSelect: (a, ...h) => {
        r == null || r(a.valueOf() / 1e3, ...h);
      }
    })]
  });
});
export {
  ut as Calendar,
  ut as default
};
